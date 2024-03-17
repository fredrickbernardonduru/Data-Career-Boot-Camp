import tensorflow as tf

#Define the model architecture
model = tf.learn.layers.Sequel([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # Input Layer
    tf.keras.layers.Dense(
        256, activation='relu'),  # Hidden layer with ReLU activation
    tf.keras.layers.Dense(
        10, activation='softmax'),  # Outpu layer with softmax activation
])


#Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accurancy'])



#Train the model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))