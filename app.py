import os
import shutil
import subprocess

# Define source and destination paths
source_dir = r"C:\Users\haric\Downloads\plantnet_300K\images"
destination_dir = r"C:\Users\haric\Downloads\project\pl\latestt\plantdataset"

# Define the folders to process
folders = ['test', 'train', 'val']

def move_and_push():
    for folder in folders:
        source_path = os.path.join(source_dir, folder)
        dest_path = os.path.join(destination_dir, folder)
        
        # Get the list of subfolders
        subfolders = [f for f in os.listdir(source_path) if os.path.isdir(os.path.join(source_path, f))]

        # Process in batches of 3 subfolders
        for i in range(0, len(subfolders), 3):
            batch = subfolders[i:i + 3]
            
            # Move each subfolder to the destination
            for subfolder in batch:
                shutil.move(os.path.join(source_path, subfolder), dest_path)
                print(f"Moved {subfolder} from {source_path} to {dest_path}")

            # Git commands
            os.chdir(destination_dir)
            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", f"Moved 3 {folder} subfolders"])
            subprocess.run(["git", "push", "origin", "main"])

            print(f"Pushed {folder} subfolders to GitHub.")

if __name__ == "__main__":
    move_and_push()
