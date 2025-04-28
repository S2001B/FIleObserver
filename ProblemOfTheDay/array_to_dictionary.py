def flatten_file_structure(file_paths: list[str]) -> dict:
    
    child_list = list()
    parent_list = list()

    for entry in file_paths:
        parent, child = entry.split("/")

        if child not in child_list:
            child_list.append(child)
            parent_list.append(parent)

            print(child_list)
            print(parent_list)

    return dict(zip(child_list, parent_list))

print(flatten_file_structure(["downloads/invoice.pdf", "downloads/report.docx", "temp/invoice.pdf", "rejected/old_data.csv"]))

""" GPT VERSION ->

def flatten_file_structure(file_paths: list[str]) -> dict:
    result = {}
    for entry in file_paths:
        folder, filename = entry.split("/")
        if filename not in result:
            result[filename] = folder
    return result 

"""
