from setuptools import setup, find_packages

setup(
    name='audio-diffusion-sketchbook',
    version='1.0.0',
    url='https://github.com/lonewater/audio-diffusion-sketchbook.git',
    author='Zach Evans, Andrew Parker',
    packages=find_packages(),    
    dependency_links=[
        "https://github.com/caillonantoine/cached_conv.git#egg=cached_conv",
        "https://github.com/caillonantoine/UDLS.git#egg=udls",
    ],
    install_requires=[
        'auraloss',
        'einops',
        'pytorch_lightning', 
        'torch',
        'torchaudio',
        'wandb',
        'cached_conv @ git+https://github.com/caillonantoine/cached_conv.git#egg=cached_conv',
        'udls @ https://github.com/caillonantoine/UDLS.git#egg=udls'
    ],
)