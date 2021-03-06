# pylint: disable=no-self-use,invalid-name
import pytest

from srl_model.common import Params
from srl_model.common.checks import ConfigurationError
from srl_model.modules import Seq2SeqEncoder
from srl_model.common.testing import AllenNlpTestCase


class TestSeq2SeqEncoder(AllenNlpTestCase):
    def test_from_params_builders_encoder_correctly(self):
        # We're just making sure parameters get passed through correctly here, and that the basic
        # API works.
        params = Params({
                "type": "lstm",
                "bidirectional": True,
                "num_layers": 3,
                "input_size": 5,
                "hidden_size": 7
                })
        encoder = Seq2SeqEncoder.from_params(params)
        # pylint: disable=protected-access
        assert encoder.__class__.__name__ == 'PytorchSeq2SeqWrapper'
        assert encoder._module.__class__.__name__ == 'LSTM'
        assert encoder._module.num_layers == 3
        assert encoder._module.input_size == 5
        assert encoder._module.hidden_size == 7
        assert encoder._module.bidirectional is True
        assert encoder._module.batch_first is True

    def test_from_params_requires_batch_first(self):
        params = Params({
                "type": "lstm",
                "batch_first": False,
                })
        with pytest.raises(ConfigurationError):
            # pylint: disable=unused-variable
            encoder = Seq2SeqEncoder.from_params(params)
