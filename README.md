# Git Workflow Assistant

## Description
Git Workflow Assistant is a command-line interface (CLI) tool that automates common Git workflows, such as initializing repositories, branching, merging, committing, and pushing changes. This tool simplifies Git operations, making it easier for developers to manage their repositories.

## Features
- **Initialize Git Repository**: Quickly initialize a new Git repository.
- **Branch Management**: Create, switch, and list branches effortlessly.
- **Commit Changes**: Commit changes with a specified commit message.
- **Push Changes**: Push local changes to a remote repository.
- **Merge Branches**: Merge one branch into another.
- **Interactive Mode**: User-friendly interactive mode to select actions from a menu.
- **Configuration File**: Supports configuration file to set default options.
- **Logging**: Logs actions performed for debugging and tracking changes.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/mgiannopoulos24/Git-Workflow-Assistant.git
    ```

2. **Navigate to the Repository Directory**:
    ```sh
    cd Git-Workflow-Assistant
    ```

3. **Install the Requirements**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create Configuration File (Optional)**:
    Create a `git_workflow_config.yaml` file in the repository directory with the following content:
    ```yaml
    default_remote: origin
    default_branch: main
    ```

## Usage

The Git Workflow Assistant can be used by executing the `cli.py` script followed by the desired action and options.

### Available Actions

- `init`: Initialize a new Git repository.
    ```sh
    python3 cli.py init
    ```

- `branch`: Create a new branch. Requires `--branch` option.
    ```sh
    python3 cli.py branch --branch <branch_name>
    ```

- `switch`: Switch to an existing branch. Requires `--branch` option.
    ```sh
    python3 cli.py switch --branch <branch_name>
    ```

- `list`: List all branches.
    ```sh
    python3 cli.py list
    ```

- `commit`: Commit changes with a message. Requires `--message` option.
    ```sh
    python3 cli.py commit --message "<commit_message>"
    ```

- `push`: Push changes to a remote repository. Optionally specify `--remote` and `--branch`.
    ```sh
    python3 cli.py push --remote <remote_name> --branch <branch_name>
    ```

- `merge`: Merge one branch into another. Requires `--source` and `--target` options.
    ```sh
    python3 cli.py merge --source <source_branch> --target <target_branch>
    ```

- `interactive`: Start the interactive mode.
    ```sh
    python3 cli.py interactive
    ```

### Examples

1. **Initialize a Repository**:
    ```sh
    python3 cli.py init
    ```

2. **Create a New Branch**:
    ```sh
    python3 cli.py branch --branch feature-branch
    ```

3. **Switch to an Existing Branch**:
    ```sh
    python3 cli.py switch --branch feature-branch
    ```

4. **List All Branches**:
    ```sh
    python3 cli.py list
    ```

5. **Commit Changes**:
    ```sh
    python3 cli.py commit --message "Add new feature"
    ```

6. **Push Changes to a Remote Repository**:
    ```sh
    python3 cli.py push --remote origin --branch main
    ```

7. **Merge One Branch into Another**:
    ```sh
    python3 cli.py merge --source feature-branch --target main
    ```

8. **Start Interactive Mode**:
    ```sh
    python3 cli.py interactive
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contact

If you have any questions or feedback, feel free to open an issue or contact the project maintainer.

---

Thank you for using Git Workflow Assistant! I hope it makes your Git experience more enjoyable and productive.
