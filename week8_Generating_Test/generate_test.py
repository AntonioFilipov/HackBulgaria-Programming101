
def read_file(file_name):
    read_file = open(file_name, "r")
    content = read_file.read()
    read_file.close()
    return content


def set_name_of_test_file(read_file):
    split_name = read_file.split('.')
    test_name = "{}.py".format(split_name[0])
    return test_name


def split_file_content(filename):
    read_file_content = read_file(filename)
    split_content = read_file_content.split("\n")
    return split_content


def get_description_of_test_file(split_content):
    for item in split_content:
        if "import" in item:
            continue
        else:
            description = item
            break
    return description


def get_imports(split_content):
    imports = []
    for item in split_content:
        if "import" in item:
            imports.append(item)
        else:
            break
    return imports


def set_test_class_name(file_name):
    domein = file_name.split('.')[0]
    split_domein = domein.split('_')
    class_name = ""
    for item in split_domein:
        class_name += item.title()
    return class_name


def get_test_cases(split_content):
    test_cases = []
    for item in split_content:
        if "->" in item:
            test_cases.append(item)
    return test_cases


def get_test_case_function(test_cases):
    functions = []
    for item in test_cases:
        functions.append(item.split("->")[1].split("==")[0].strip())
    return functions


def get_test_case_description(test_cases):
    descriptions = []
    for item in test_cases:
        descriptions.append(item.split("->")[0].strip())
    return descriptions


def make_test_file(filename):
    test_file_content = []
    test_file_content.append("import unittest")
    split_content = split_file_content(filename)
    imports = get_imports(split_content)
    for item in imports:
        test_file_content.append("{}".format(item))
    test_file_content.append("\n\nclass {}(unittest.TestCase):".format(set_test_class_name(filename)))
    file_description = get_description_of_test_file(split_content)
    test_file_content.append("    {}".format(file_description))
    test_cases = get_test_cases(split_content)
    for i, item in enumerate(test_cases):
        test_file_content.append("\n    def testCase{}(self):".format(i+1))
        functions = get_test_case_function(test_cases)
        description = get_test_case_description(test_cases)
        if "True" in item:
            test_file_content.append("        self.assertTrue({}, {})".format(functions[i], description[i]))
        else:
            test_file_content.append("        self.assertFalse({}, {})".format(functions[i], description[i]))
    test_file_content.append("if __name__ == '__main__':")
    test_file_content.append("    unittest.main()")
    return test_file_content


def create_test_file(test_file_name, test_file_content):
    write_file = open(test_file_name, "w")
    for item in test_file_content:
        write_file.write(item + '\n')
    write_file.close()


def main():
    filename = "is_prime_test.dsl"
    test_file_name = set_name_of_test_file(filename)
    test_file_content = make_test_file(filename)
    create_test_file(test_file_name, test_file_content)

if __name__ == '__main__':
    main()