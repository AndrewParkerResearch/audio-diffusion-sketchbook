from setuptools import setup, find_packages

setup(
    name='audio-diffusion',
    version='1.0.0',
    url='https://github.com/zqevans/audio-diffusion.git',
    author='Zach Evans',
    packages=find_packages(),    
    install_requires=[
        'torch',
        'torchaudio',
        'pytorch_lightning', 
        'wandb'
    ],
)