import argparse
from git_workflow_assistant import GitWorkflowAssistant

def interactive_mode():
    assistant = GitWorkflowAssistant()
    actions = {
        '1': 'init',
        '2': 'branch',
        '3': 'switch',
        '4': 'list',
        '5': 'commit',
        '6': 'push',
        '7': 'merge'
    }

    print("Select an action:")
    print("1. Initialize Repository")
    print("2. Create Branch")
    print("3. Switch Branch")
    print("4. List Branches")
    print("5. Commit Changes")
    print("6. Push Changes")
    print("7. Merge Branches")

    choice = input("Enter the number of the action: ")
    action = actions.get(choice)
    if not action:
        print("Invalid choice")
        return

    if action == 'init':
        print(assistant.init_repo())
    elif action == 'branch':
        branch_name = input("Enter branch name: ")
        print(assistant.create_branch(branch_name))
    elif action == 'switch':
        branch_name = input("Enter branch name: ")
        print(assistant.switch_branch(branch_name))
    elif action == 'list':
        print(assistant.list_branches())
    elif action == 'commit':
        message = input("Enter commit message: ")
        print(assistant.commit_changes(message))
    elif action == 'push':
        remote = input("Enter remote name (default: origin): ") or 'origin'
        branch = input("Enter branch name (default: main): ") or 'main'
        print(assistant.push_changes(remote, branch))
    elif action == 'merge':
        source = input("Enter source branch: ")
        target = input("Enter target branch: ")
        print(assistant.merge_branch(source, target))

def main():
    parser = argparse.ArgumentParser(description='Git Workflow Assistant')
    parser.add_argument('action', choices=['init', 'branch', 'switch', 'list', 'commit', 'push', 'merge', 'interactive'], help='Action to perform')
    parser.add_argument('--branch', help='Branch name for create or switch action')
    parser.add_argument('--message', help='Commit message for commit action')
    parser.add_argument('--source', help='Source branch for merge action')
    parser.add_argument('--target', help='Target branch for merge action')
    parser.add_argument('--remote', default='origin', help='Remote repository for push action')
    parser.add_argument('--repo_path', default='.', help='Path to the repository')

    args = parser.parse_args()
    assistant = GitWorkflowAssistant(args.repo_path)

    try:
        if args.action == 'interactive':
            interactive_mode()
        elif args.action == 'init':
            print(assistant.init_repo())
        elif args.action == 'branch':
            if not args.branch:
                raise ValueError('Branch name required for branch action')
            print(assistant.create_branch(args.branch))
        elif args.action == 'switch':
            if not args.branch:
                raise ValueError('Branch name required for switch action')
            print(assistant.switch_branch(args.branch))
        elif args.action == 'list':
            print(assistant.list_branches())
        elif args.action == 'commit':
            if not args.message:
                raise ValueError('Commit message required for commit action')
            print(assistant.commit_changes(args.message))
        elif args.action == 'push':
            print(assistant.push_changes(args.remote, args.branch))
        elif args.action == 'merge':
            if not args.source or not args.target:
                raise ValueError('Source and target branches required for merge action')
            print(assistant.merge_branch(args.source, args.target))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
