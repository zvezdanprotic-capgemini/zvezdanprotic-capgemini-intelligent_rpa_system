import xml.etree.ElementTree as ET
import os

def read_bpmn_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        # Parse the BPMN XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Print process details
        for process in root.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}process"):
            print(f"Process ID: {process.get('id')}, Name: {process.get('name')}")

            # Print task details
            for task in process.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}task"):
                print(f"  Task ID: {task.get('id')}, Name: {task.get('name')}")

    except ET.ParseError as e:
        print(f"Error parsing BPMN file: {e}")


def print_data_object_references(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        # Parse the BPMN XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Print data object references
        for process in root.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}process"):
            print(f"\nProcess ID: {process.get('id')}, Name: {process.get('name')}")
            for data_object in process.findall(".//{http://www.omg.org/spec/BPMN/20100524/MODEL}dataObjectReference"):
                print(f"  Data Object ID: {data_object.get('id')}, Name: {data_object.get('name')}")

    except ET.ParseError as e:
        print(f"Error parsing BPMN file: {e}")

# Example usage
if __name__ == "__main__":
    bpmn_file_path = "loan_process.bpmn"  # Replace with the path to your BPMN file
    read_bpmn_file(bpmn_file_path)
    print_data_object_references(bpmn_file_path)