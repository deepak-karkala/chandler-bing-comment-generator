git clone h^C.com/deepak-karkala/chandler-bing-comment-generator.git
cd chandler-bing-comment-generator/
conda create -n handbook python=3.10
conda init
source /home/ec2-user/anaconda3/etc/profile.d/conda.sh
conda activate handbook
python -m pip install .
python -m pip install flash-attn --no-build-isolation
huggingface-cli login