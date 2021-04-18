import numpy as np
import onnx

from tests.tools import expect


class Sum:
    @staticmethod
    def export():  # type: () -> None
        data_0 = np.array([3, 0, 2]).astype(np.float32)
        data_1 = np.array([1, 3, 4]).astype(np.float32)
        data_2 = np.array([2, 6, 6]).astype(np.float32)
        result = np.array([6, 9, 12]).astype(np.float32)
        node = onnx.helper.make_node(
            'Sum',
            inputs=['data_0', 'data_1', 'data_2'],
            outputs=['result'],
        )
        expect(
            node,
            inputs=[data_0, data_1, data_2],
            outputs=[result],
            name='test_sum_example',
        )

        node = onnx.helper.make_node(
            'Sum',
            inputs=['data_0'],
            outputs=['result'],
        )
        expect(node, inputs=[data_0], outputs=[data_0], name='test_sum_one_input')

        result = np.add(data_0, data_1)
        node = onnx.helper.make_node(
            'Sum',
            inputs=['data_0', 'data_1'],
            outputs=['result'],
        )
        expect(
            node, inputs=[data_0, data_1], outputs=[result], name='test_sum_two_inputs'
        )


if __name__ == '__main__':
    Sum.export()
