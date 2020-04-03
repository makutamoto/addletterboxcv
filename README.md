# Add Letterbox CV
[![Build Status](https://travis-ci.org/makutamoto/addletterboxcv.svg?branch=master)](https://travis-ci.org/makutamoto/addletterboxcv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
Add a letterbox to the video and scale it to the specified size.  
Note: this program does not support audio.

## Usage
```
usage: addletterboxcv [-h] --dimension WIDTH HEIGHT
                   [--interpolation {NEAREST,LINEAR,AREA,CUBIC,LANCZOS4}]
                   [--codec CODEC]
                   video output
```