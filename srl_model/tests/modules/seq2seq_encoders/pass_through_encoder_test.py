# pylint: disable=no-self-use,invalid-name
import torch
import numpy

from srl_model.common.testing import AllenNlpTestCase
from srl_model.modules.seq2seq_encoders import PassThroughEncoder


class TestStackedSelfAttention(AllenNlpTestCase):
    def test_get_dimension_is_correct(self):
        encoder = PassThroughEncoder(input_dim=9)
        assert encoder.get_input_dim() == 9
        assert encoder.get_output_dim() == 9

    def test_pass_through_encoder_passes_through(self):
        encoder = PassThroughEncoder(input_dim=9)
        tensor = torch.randn([2, 3, 9])
        output = encoder(tensor)
        numpy.testing.assert_array_almost_equal(tensor.detach().cpu().numpy(),
                                                output.detach().cpu().numpy())
