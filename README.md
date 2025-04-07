# Gemini Automator
Most AI image generators like ChatGPT charge you after a few free generations. Gemini, on the other hand, lets you generate as many images as you want—for free. But it can only generate one image per prompt. That means you have to wait for each generation to finish before you can submit the next one, which quickly becomes time-consuming. Gemini Automator solves that problem.

It automatically feeds prompts from a prompts.txt file into Gemini, one by one—just like a human would. No need to sit in front of your computer typing each command. It even mimics human behavior to avoid getting flagged by Google or triggering a CAPTCHA, so everything runs smoothly and uninterrupted. It leverages Selenium to interact with Gemini's AI image generation platform.

## Features

- Automates the process of generating images from text prompts on Gemini.
- Types prompts automatically into Gemini's input area.
- Fetches the generated image URL after the prompt is processed.
- Can be easily customized for other image generation platforms.

## Requirements

- **Python 3.x**: Make sure Python is installed on your system.
- **Selenium**: Web automation library to interact with browsers.
- **Chrome Browser**: Chrome is used for automation with your own profile.

### Install Required Python Libraries

Run the following command to install the necessary Python libraries:

```bash
pip install selenium
```

## How to Use It

### Step 1: Open Chrome with Remote Debugging
To connect Selenium to your Chrome browser, you must start Chrome with remote debugging enabled. Open a terminal or command prompt and run:

```bash
start chrome --remote-debugging-port=9222 --user-data-dir="C:\Program Files\Google\Chrome\Application\chrome.exe""
```

This will launch Chrome with remote debugging enabled on port 9222, allowing the script to control it.

Note: Update the path to your 'chrome.exe' in the ```user-data-dir``` field if Chrome is installed in a location other than the default.

### Step 2: Run the Python Script
- Clone this repository or download the script to your local machine.
- Place your list of prompts in a file called prompts.txt (each prompt on a new line).

Run the script:

```bash
python script.py
```
The script will:

- Open Gemini in your Chrome browser.
- Type each prompt from prompts.txt into the input field.
- Wait for the image to be generated and output the image URL.

### Step 3: Access Generated Images
Once the script completes, the image URLs will be displayed in your chatbox within the Gemini interface.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Contributions are always welcome!

## Credit
Gemini Automator has been solely developed by Soad.
