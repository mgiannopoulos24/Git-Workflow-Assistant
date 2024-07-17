import subprocess
import yaml
import os
import logging

class GitWorkflowAssistant:
    def __init__(self, repo_path='.'):
        self.repo_path = repo_path
        self.config = self.load_config()
        self.setup_logging()

    def load_config(self):
        config_path = os.path.join(self.repo_path, 'git_workflow_config.yaml')
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        return {}

    def get_config_option(self, option, default=None):
        return self.config.get(option, default)

    def setup_logging(self):
        logging.basicConfig(filename='git_workflow_assistant.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log(self, message):
        logging.info(message)

    def run_git_command(self, command):
        self.log(f"Running command: {' '.join(command)}")
        try:
            result = subprocess.run(command, cwd=self.repo_path, text=True, capture_output=True)
            result.check_returncode()
            self.log(f"Command succeeded: {' '.join(command)}")
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.log(f"Command failed: {' '.join(command)} - {e.stderr}")
            raise Exception(f"Git command failed: {e.stderr}") from e
        except Exception as e:
            self.log(f"Unexpected error: {str(e)}")
            raise Exception(f"An unexpected error occurred: {str(e)}") from e

    def init_repo(self):
        return self.run_git_command(['git', 'init'])

    def create_branch(self, branch_name):
        return self.run_git_command(['git', 'checkout', '-b', branch_name])

    def switch_branch(self, branch_name):
        return self.run_git_command(['git', 'checkout', branch_name])

    def list_branches(self):
        return self.run_git_command(['git', 'branch'])

    def commit_changes(self, message):
        return self.run_git_command(['git', 'commit', '-m', message])

    def push_changes(self, remote=None, branch=None):
        remote = remote or self.get_config_option('default_remote', 'origin')
        branch = branch or self.get_config_option('default_branch', 'main')
        return self.run_git_command(['git', 'push', remote, branch])

    def merge_branch(self, source_branch, target_branch):
        self.switch_branch(target_branch)
        return self.run_git_command(['git', 'merge', source_branch])
