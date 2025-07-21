from backend1 import WSMVideogameClassifier
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WSM Videogame Classifier CLI")
    parser.add_argument("train_file", type=str, help="Path to the training Excel file")
    parser.add_argument("results_file", type=str, help="Path to the results Excel file")
    args = parser.parse_args()
    classifier = WSMVideogameClassifier(args.train_file, args.results_file)
    classifier.f_main_pipeline()
