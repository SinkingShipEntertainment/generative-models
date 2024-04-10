name = 'sgm'

version = '0.1.0'

authors = [
    'Stability AI',
]

description = '''Generative model'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
    "black-23.7.0",
    "chardet-5.1.0",
    "clip",
    "einops",
    "fairscale",
    "fire",
    "fsspec",
    "invisible-watermark",
    "kornia-0.6.9",
    "matplotlib",
    "natsort",
    "ninja",
    "numpy",
    "omegaconf",
    "open-clip-torch",
    "opencv-python-4.6.0.66",
    "pandas",
    "pillow",
    "pudb",
    "pytorch-lightning-2.0.1",
    "pyyaml",
    "rembg",
    "scipy",
    "streamlit",
    "tensorboardx-2.6",
    "timm",
    "tokenizers-0.12.1",
    "torch",
    "torchaudio",
    "torchdata-0.6.1",
    "torchmetrics",
    "torchvision",
    "tqdm",
    "transformers-4.19.1",
    "triton-2.0.0",
    "urllib3-1.26",
    "wandb",
    "webdataset",
    "wheel",
    "xformers",
    "gradio",
    "streamlit-keyup-0.2.0",
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_SGM_ROOT = '{root}'
    env.PYTHONPATH.append('{root}')


build_command = 'rez python {root}/rez_build.py'
uuid = 'repository.generative-models'

