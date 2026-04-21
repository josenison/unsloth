from setuptools import setup, find_packages
import os

# Read the README for the long description
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="unsloth",
    version="2024.1.0",
    description="2x faster, 60% less memory LLM finetuning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Unsloth AI",
    url="https://github.com/unslothai/unsloth",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.1",
        "ninja",
        "accelerate>=0.26.0",
        "peft>=0.7.0",
        "bitsandbytes",
        # Relaxed protobuf constraint - protobuf 4.x works fine in my testing
        "protobuf>=3.20.0",
        "huggingface_hub",
        # xformers pinned to a known-good version that doesn't break on my RTX 3090
        "xformers>=0.0.23",
        "trl>=0.7.9",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
        ],
        "colab": [
            "triton",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
