import numpy, os, pandas


class WSMVideogameClassifier:
    def __init__(self, c1_train_file: str, c1_results_file: str):
        self.train_file = c1_train_file
        self.results_file = c1_results_file

    @staticmethod
    def __f_frequency_calculation(f1_df) -> list:
        if f1_df.empty:
            raise ValueError("DataFrame is empty")
        if f1_df.shape[1] < 2:
            raise ValueError("DataFrame must have at least two columns")
        f1_df_rows: int = len(f1_df)
        f1_category_columns: list = list(f1_df.columns[1:])
        try:
            f1_sum_per_category: list = list(f1_df[f1_category_columns].sum(axis=0))
        except ValueError as e:
            raise ValueError("Error while summing category columns") from e
        return [round(_/f1_df_rows,2) for _ in f1_sum_per_category]

    @staticmethod
    def __f_score_calculation(f2_df, f2_frequency_per_category: list) -> list:
        f2_values_per_game: list = [list(_)[2:] for _ in f2_df.itertuples()]
        try:
            f2_points_per_game: list = \
                [numpy.round(numpy.dot(f2_frequency_per_category, _), 2) for _ in f2_values_per_game]
        except ValueError as e:
            raise ValueError("Error while summing category columns") from e
        return [round(_ * 10 / sum(f2_frequency_per_category), 1) for _ in f2_points_per_game]

    @staticmethod
    def __f_write_file(f3_str:str, f3_df, f3_results: list) -> None:
        if not isinstance(f3_str, str) or '.' not in f3_str:
            raise ValueError("Expected a valid filename string with extension.")
        if not isinstance(f3_results, list):
            raise TypeError("f3_results must be a list.")
        f3_name_txt_file: str = "Results " + os.path.splitext(os.path.basename(f3_str))[0] + ".txt"
        try:
            f3_vg_names: list = [list(_)[1] for _ in f3_df.itertuples()]
        except ValueError as e:
            raise ValueError("Length of f3_results must match number of rows in f3_df.") from e
        f3_results_dict_sorted: list = (
            sorted(dict(zip(f3_vg_names, f3_results)).items(), key=lambda item: item[1], reverse=True))
        try:
            with open(f3_name_txt_file, "w", encoding="utf-8") as f3_file:
                f3_file.write("Result score out of 10 for each videogame according to prefered type of play:\n\n")
                for _ in f3_results_dict_sorted:
                    f3_file.write(f"{_[0]}: {_[1]}\n")
        except OSError as e:
            raise OSError(f"Failed to write file '{f3_name_txt_file}': {e}")
        print(f"Result file saved in the Python script directory as: {os.path.abspath(f3_name_txt_file)}")
        return None

    def f_main_pipeline(self) -> None:
        try:
            f4_df_train_values = pandas.read_excel(self.train_file).fillna(0)
            f4_frequency_values: list = self.__f_frequency_calculation(f4_df_train_values)
            if self.train_file == self.results_file:
                f4_test_results: list = self.__f_score_calculation(f4_df_train_values, f4_frequency_values)
                self.__f_write_file(self.results_file, f4_df_train_values, f4_test_results)
                return None
            f4_df_results = pandas.read_excel(self.results_file).fillna(0)
            f4_test_results: list = self.__f_score_calculation(f4_df_results, f4_frequency_values)
            self.__f_write_file(self.results_file, f4_df_results, f4_test_results)
            return None
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except PermissionError as e:
            print(f"Permission error: {e}")
        except ValueError as e:
            print(f"Value error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    WSMVideogameClassifier_object = WSMVideogameClassifier("WSM Types Play VG Train.xlsx",
                                                           "WSM Types Play VG Train.xlsx")
    WSMVideogameClassifier_object.f_main_pipeline()
