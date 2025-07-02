# ✨ gif-maker
> A tiny but aesthetic Python tool that turns images into ✨GIFs✨ — made by [@avocadoyoon](https://github.com/avocadoyoon) 💚

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="250" alt="GIF Vibes"/>
</p>

## 📸 What is this?

This is a minimal Python script that takes a list of image files and stitches them into a looping GIF.  
Perfect for welcome screens, memes, art portfolios, or just spamming your friends with vibes.

## 🚀 How it works

In `create_gif.py`, the script:
- Loads image files (`welcome1.jpeg`, `welcome2.jpeg`, `welcome3.jpeg`)
- Converts them into frames
- Creates a `hi.gif` that loops forever, with a 0.9s delay per frame

```python

import imageio.v3 as iio

filenames = ['welcome1.jpeg', 'welcome2.jpeg', 'welcome3.jpeg']
images = [iio.imread(filename) for filename in filenames]
iio.imwrite('hi.gif', images, duration=900, loop=0)

🧪 Requirements
pip install imageio

🎮 How to run
Put your images in the same folder as the script, then:
`python create_gif.py`

Tada! You’ll get a cute lil `hi.gif` in your folder ✨

🪄 Customizing
Want to make your own vibe? Just swap out the image filenames:
`filenames = ['cool1.png', 'cool2.png', 'cool3.png']`

And change the output name:
`iio.imwrite('myCoolGif.gif', ...)`

You can also:
Adjust duration=900 (milliseconds per frame)
Set loop=0 for an infinite loop, or loop=1 to stop after one run

🧁 Future ideas
-Add command-line arguments for file names and speed
-Add support for sorting images automatically
-Turn it into a Streamlit drag-and-drop web app?


by @avocadoyoon, probably while drinking coffee and listening to lo-fi
💬 Feel free to fork, star, or collab!
