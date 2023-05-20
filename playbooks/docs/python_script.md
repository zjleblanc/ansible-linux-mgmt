# python_script

This playbook takes the output of a custom python script and demonstrates how to use it in subsequent tasks.

## suggested use case

If you have a custom python script that extracts information from any data source (i.e. Excel, web scrape, logs, etc.) and you want to use that as an input to your ansible playbook.
<br>
<br>
If you are creating a python script from scratch, I **do not recommend** this method and instead point you at the documentation for creating Ansible modules. Modules are typically developed in Python and will simplify the integration of your efforts into automation tasks.

### important notes

The module used to execute a script is called `ansible.builtin.script`. When you call a script from ansible, it generally looks something like this:

```yaml
- name: Run script
  register: r_script_output
  args:
    executable: python3
  ansible.builtin.script: "path/to/your/script.py" # this can also be a variable
```

The return object, registered to `r_script_output` in my example, will have a few keys of interest:
```json
{
    "rc": 0, // the return code
    "stderr": "raw string of anything written to standard error",
    "stdout": "raw string of anything written to standard out",
    "stdout_lines": "standard out lines in the form of an array",
}
```

Given successful execution of your script, you will likely consume either **stdout** or **stdout_lines**. When combining a script with Ansible, I generally like to dump a single object as json in my script and use the **stdout** return key. I prefer this method because you can pipe it to a standard filter plugin and treat it as a structured dictionary from then on. Below is what that looks like on the python side and the ansible side:

```python
# path/to/your/script.py
import json
...
data = {"name": "zach", "company": "Red Hat"}
print(json.dumps(data))
```

Two important steps in the python script worth noting:
1. Use of `print(...)` will register the output in **stdout**. If you are using the python logging library, then you must configure it to pipe to standard out or do some nasty parsing of the **stderr** value in ansible.
1. Use of `json.dumps(...)` will output your python data as a string which will enable the `from_json` filter plugin to work as expected. Without dumping, you will see some red 🙃

```yaml
...

- name: Use filter plugin to transform stdout to structured dictionary
  ansible.builtin.set_fact:
    # from_json is a filter plugin included in ansible
    python_data: "{{ r_script_output.stdout | from_json }}" 

- name: Example using the python data
  ansible.builtin.debug:
    msg: "{{ python_data.name }} works for {{ python_data.company }}"
...
```

I admit this example uses a very simple data structure, but the method will work for any json structure from python -> ansible. That gives you a lot of flexibility to consume output from existing python scripts. If you are looking for a challenge, try rewriting your script to be an Ansible module!
