import os
from file_name_manipulation import rename_file

current_folder = os.path.dirname(os.path.relpath(__file__))

def process_files(file_list: list):

    log = os.path.join(current_folder, "log.txt")

    if not os.path.exists(log):
        open(log, "w").close()

    with open(log, "a") as writer:

        for file in file_list:
            result = rename_file(file)

            if result == file:
                writer.write(f"No change for |{result}|\n")
            else:
                writer.write(f"Renamed |{file}| to |{result}|\n")


if __name__ == "__main__":
    print("Running file!")


# file_list = [
#     "invoice april final.pdf",
#     "Invoice_DRAFT.PDF",
#     "shopping list.txt",
#     "invoice_2025_march.docx",
#     " budget_report.pdf",
#     "random file.txt"
# ]


# print(process_files(file_list))
