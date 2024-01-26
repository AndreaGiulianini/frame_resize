## Summary

This project provides a simple tool to resize images with added white borders, allowing users to adjust the size of images while maintaining a consistent aspect ratio. The tool is packaged as a Docker container for ease of deployment and includes a Python script (`resize_images.py`) that performs the resizing operation.

## Description

The primary functionality of the script involves opening an image file, resizing it with a specified percentage increase, and adding white borders to maintain the original aspect ratio. The percentage increase for white borders is customizable, providing flexibility in the resizing process.

## Use Case

This tool is particularly useful for scenarios where a batch of images needs to be resized uniformly, such as in preparing images for a website, presentation, or any other use case where maintaining a consistent visual appearance is essential.

## Command for start project

`docker build -t resize-images .`

`docker run -v ./photo:/app/input -v ./photo_output:/app/output resize-images --percentage_increase 20`
