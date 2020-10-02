#!/usr/bin/env python3
from os import getenv, path


def pid_from_cwd():
    """Returns a project's ID based on the current working directory"""
    cwd = path.basename(getenv('PWD'))
    sedo_list = [{205: "0x00-shell_basics"},
                 {207: "0x01-shell_permissions"}, {208: "0x02-shell_redirections"}, {209: "0x03-shell_variables_expansions"}, {251: "0x04-loops_conditions_and_parsing"}, {255: "0x05-processes_and_signals"}, {78: "0x06-regular_expressions"}, {259: "0x07-networking_basics"}, {285: "0x08-networking_basics_2"}, {302: "0x09-web_infrastructure_design"}, {292: "0x0A-configuration_management"}, {244: "0x0B-ssh"}, {266: "0x0C-web_server"}, {265: "0x0D-web_stack_debugging_0"}, {271: "0x0E-web_stack_debugging_1"}, {275: "0x0F-load_balancer"}, {276: "0x10-https_ssl"}, {298: "0x11-what_happens_when_your_type_holbertonschool_com_in_your_browser_and_press_enter"}, {287: "0x12-web_stack_debugging_2"}, {284: "0x13-firewall"}, {280: "0x14-mysql"}, {269: "0x15-api"}, {314: "0x16-api_advanced"}, {293: "0x17-web_stack_debugging_3"}, {281: "0x18-webstack_monitoring"}, {294: "0x19-postmortem"}]
    low_list = [{212: "0x00-hello_world"},
                {213: "0x01-variables_if_else_while"}, {214: "0x02-functions_nested_loops"}, {539: "0x03-debugging"}, {215: "0x04-more_functions_nested_loops"}, {216: "0x05-pointers_arrays_strings"}, {217: "0x06-pointers_arrays_strings"}, {218: "0x07-pointers_arrays_strings"}, {219: "0x08-recursion"}, {220: "0x09-static_libraries"}, {221: "0x0A-argc_argv"}, {222: "0x0B-malloc_free"}, {223: "0x0C-more_malloc_free"}, {224: "0x0D-preprocessor"}, {225: "0x0E-structures_typedef"}, {226: "0x0F-function_pointers"}, {227: "0x10-variadic_functions"}, {228: "printf"}, {229: "0x12-singly_linked_lists"}, {230: "0x13-more_singly_linked_lists"}, {232: "0x14-bit_manipulation"}, {234: "0x15-file_io"}, {235: "simple_shell"}, {240: "0x17-doubly_linked_lists"}, {242: "0x18-dynamic_libraries"}, {249: "monty"}, {253: "0x1A-hash_tables"}, {248: "sorting_algorithms"}, {273: "0x1C-makefiles"}, {270: "binary_trees"}, {295: "0x1E-search_algorithms"}]
    high_list = [{231: "0x00-python-hello_world"}, {233: "0x01-python-if_else_loops_functions"}, {239: "0x02-python-import_modules"}, {241: "0x03-python-data_structures"}, {243: "0x04-python-more_data_structures"}, {245: "0x05-python-exceptions"}, {247: "0x06-python-classes"}, {246: "0x07-python-test_driven_development"}, {250: "0x08-python-more_classes"}, {252: "0x09-python-everything_is_object"},
                 {254: "0x0A-python-inheritance"}, {260: "0x0B-python-input_output"}, {331: "0x0C-python-almost_a_circle"}, {272: "0x0D-SQL_introduction"}, {274: "0x0E-SQL_more_queries"}, {283: "0x0F-python-object_relational_mapping"}, {299: "0x10-python-network_0"}, {300: "0x11-python-network_1"}, {303: "0x12-javascript-warm_up"}, {304: "0x13-javascript_objects_scopes_closures"}, {333: "0x14-javascript-web_scraping"}, {305: "0x15-javascript-web_jquery"}]
    projects = {"sedo": sedo_list, "low": low_list, "high": high_list}
    all_projects = list(projects.values())
    # all projects is list of list of dicts where each dict is a project
    for track in all_projects:
        # track is a list of dicts where each dict is a project in that track
        for project in track:
            project_dir = list(project.values())[0]
            project_id = list(project.keys())[0]
            if cwd == project_dir:
                return project_id


def parent_from_cwd():
    """Returns the parent directory based on the current working directory"""
    parent = getenv('PWD').split('/')[-2]
    project_dir = getenv('PWD').split('/')[-1]
    return parent, project_dir
