#!/usr/bin/env python3

import os
import argparse
import sys

def consolidate_nvim_config(input_dir, output_file):
    """
    Crawls a directory, reads all files, and consolidates their content
    into a single output file, marking the origin of each section.

    Args:
        input_dir (str): The path to the NeoVim config directory to crawl.
        output_file (str): The path to the file where the consolidated content will be saved.
    """
    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory not found: {input_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Starting consolidation from '{input_dir}' into '{output_file}'...")

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Walk through the directory tree
            for root, dirs, files in os.walk(input_dir):
                # Sort directories and files for consistent order
                dirs.sort()
                files.sort()

                for filename in files:
                    file_path = os.path.join(root, filename)
                    # Calculate relative path for cleaner identification
                    relative_path = os.path.relpath(file_path, input_dir)

                    print(f"Processing: {relative_path}")

                    # Write a header marker to the output file
                    outfile.write(f"\n{'='*10} START: {relative_path} {'='*10}\n\n")

                    try:
                        # Open and read the content of the current file
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            content = infile.read()
                            outfile.write(content)
                    except Exception as e:
                        # Log if a file cannot be read, but continue processing others
                        print(f"Warning: Could not read file {relative_path}. Error: {e}", file=sys.stderr)
                        outfile.write(f"[Error reading file: {e}]\n")

                    # Write a footer marker to the output file
                    outfile.write(f"\n\n{'='*10} END: {relative_path} {'='*10}\n")

    except IOError as e:
        print(f"Error: Could not write to output file {output_file}. Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Consolidation complete. Output saved to '{output_file}'.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Consolidate NeoVim configuration files into a single file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter # Show default values in help
    )

    # Add arguments
    parser.add_argument(
        "input_dir",
        help="Path to the NeoVim configuration directory (e.g., ~/.config/nvim)."
    )
    parser.add_argument(
        "-o", "--output-file",
        default="consolidated_nvim_config.txt",
        help="Path to the output file for the consolidated configuration."
    )

    # Parse arguments from command line
    args = parser.parse_args()

    # Expand user directory symbols like ~
    input_dir_expanded = os.path.expanduser(args.input_dir)

    # Run the consolidation function
    consolidate_nvim_config(input_dir_expanded, args.output_file)

