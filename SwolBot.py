import numpy as np
import tensorflow as tf

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="posenet_mobilenet_v1_100_257x257_multi_kpt_stripped.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on random input data.
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

float_model = input_details[0]['dtype'] == np.float32
if float_model:
    template_input = (np.float32(template_input) - 127.5) / 127.5
    target_input = (np.float32(target_input) - 127.5) / 127.5
else:
  print("Not a float model")

# Set the value of the input tensor
interpreter.set_tensor(input_details[0]['index'], template_input)
# Run the calculations
interpreter.invoke()
# Extract output data from the interpreter
template_output_data = interpreter.get_tensor(output_details[0]['index'])
template_offset_data = interpreter.get_tensor(output_details[1]['index'])




input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)