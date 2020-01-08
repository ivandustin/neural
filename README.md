# Neural

Easy to use artificial neural network library in Python based from Keras library.



```shell
pip install artificial-neural-network
```



## Example

The example below creates an artificial neural network.

```python
import neural

# Create an artificial neural network that has 10 input neurons and 2 output neurons.
# It has 3 hidden layers with 40, 30, and 20 neurons for each layer respectively.
# This function returns a Keras model object.
model = neural.network(10, [40, 30, 20], 2)
```

The function above returns a [Keras Model API](https://keras.io/models/model/). See how you can train, predict, or save your model in the following.

```python
# The following trains the network, predicts, and saves the model.
# It uses the Keras API.
# You can read more about Keras API on their documentation.
model.fit(x, y, epochs=100, batch_size=10, shuffle=True, use_multiprocessing=True)
model.predict(x)
model.save("model.h5")
```

