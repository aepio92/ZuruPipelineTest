import json
import argparse
import datetime
import pkg_resources


def format_permissions(permissions):
    return permissions


def format_time_modified(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%b %d %H:%M')


# Convert size to human-readable format
def human_readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"


# Get directories normally
def list_directory_content(directory, show_hidden=False, filter_option=None):
    content_list = []
    for item in directory['contents']:
        name = item['name']
        if show_hidden or not name.startswith('.'):
            if filter_option is None or (filter_option == 'file' and 'contents' not in item) or (
                    filter_option == 'dir' and 'contents' in item):
                content_list.append(name)
    return content_list


# Get directories in listed manner
def list_directory_content_details(directory, show_hidden=False, filter_option=None):
    content_list = []
    for item in directory['contents']:
        permissions = item['permissions']  # Getting the permission status for files & directories
        size = item['size']  # Getting the size for files & directories
        time_modified = item['time_modified']  # Getting the time of modification for files & directories
        name = item['name']

        formatted_permissions = format_permissions(permissions)
        formatted_time_modified = format_time_modified(time_modified)
        formatted_size = human_readable_size(size)

        details = f"{formatted_permissions} {formatted_size} {formatted_time_modified} {name}"
        if show_hidden or not name.startswith('.'):
            if filter_option is None or (filter_option == 'file' and 'contents' not in item) or (
                    filter_option == 'dir' and 'contents' in item):
                content_list.append(details)
    return content_list


def main():
    # arguments declaration
    parser = argparse.ArgumentParser(description='List directory content in the style of ls')
    parser.add_argument('-A', action='store_true', help='List all entries including hidden ones')
    parser.add_argument('-l', action='store_true', help='List in long format')
    parser.add_argument('-r', action='store_true', help='List in reverse order')
    parser.add_argument('-t', action='store_true', help='Sort by time_modified (oldest first)')
    parser.add_argument('--filter', help='Filter the output based on option (file or dir)')
    args = parser.parse_args()

    # Checking Filter directory validation
    valid_filter_options = ['file', 'dir']
    if args.filter is not None and args.filter not in valid_filter_options:
        print(f"Error: Invalid filter option. Valid options are: {', '.join(valid_filter_options)}")
        return

    json_path = pkg_resources.resource_filename(__name__, 'structure.json')
    with open(json_path, 'r') as file:
        directory_structure = json.load(file)  # Loading the structure.json file

    if args.t:  # Sorting with time
        directory_structure['contents'] = sorted(directory_structure['contents'], key=lambda x: x['time_modified'])

    if args.r:  # sorting in Reverse order
        directory_structure['contents'] = reversed(directory_structure['contents'])

    if args.l:  # sorting in list format
        content_details = list_directory_content_details(directory_structure, args.A, args.filter)
        for detail in content_details:
            print(detail)
    else:
        top_level_content = list_directory_content(directory_structure, args.A, args.filter)
        print(" ".join(top_level_content))


if __name__ == "__main__":
    main()
