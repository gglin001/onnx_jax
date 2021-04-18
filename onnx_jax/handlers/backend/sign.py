import jax.numpy as jnp
from jax import jit

from onnx_jax.handlers.backend_handler import BackendHandler
from onnx_jax.handlers.handler import onnx_op
from onnx_jax.pb_wrapper import OnnxNode


@onnx_op("Sign")
class Sign(BackendHandler):
    @classmethod
    def _common(cls, node: OnnxNode, **kwargs):
        @jit
        def _sign(x):
            return jnp.sign(x)

        return _sign

    @classmethod
    def version_9(cls, node, **kwargs):
        return cls._common(node, **kwargs)

    @classmethod
    def version_13(cls, node, **kwargs):
        return cls._common(node, **kwargs)
