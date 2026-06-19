import os
import shutil

src_dirs = ['textures', 'models', 'splats']

for src_dir in src_dirs:
    if not os.path.exists(src_dir):
        continue
    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        dest_dir = os.path.join('.', rel_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for f in files:
            src_file = os.path.join(root, f)
            dest_file = os.path.join(dest_dir, f)
            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied {src_file} to {dest_file}")
