import pandas as pd
import xlsxwriter


class Excel:
    """
    Excel
    """

    def write_excel(self, file_path, data):
        """
        :param file_path: [String]
        :param data: [Dictionary {String: Dictionary {String: List}}]
        example data: {sheet_name: {col_name: col_values}}
        """

        if file_path == "":
            raise Exception("No file_path provided")

        if len(data) == 0:
            raise Exception("No data provided, please provide a dictionary in the following format: "
                            "{sheet_name: {col_name: col_values}}")

        with pd.ExcelWriter(file_path) as writer:
            for sheet in data:
                df = pd.DataFrame(data[sheet])
                df.to_excel(writer, sheet_name=sheet)


