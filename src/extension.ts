import * as vscode from 'vscode';

type Repository = {
    rootUri: vscode.Uri;
    state: {
        refs: { name: string }[]; // Update this line to use the correct type
    };
    inputBox: {
        commit: () => Promise<void>;
    };
};

export function activate(context: vscode.ExtensionContext) {
  const gitExtension = vscode.extensions.getExtension<{ getAPI(version: number): any }>('vscode.git')?.exports.getAPI(1);
  if (gitExtension) {
    const { repositories } = gitExtension;
    repositories.forEach((repo: any) => {
      console.log(`Repository: ${repo.rootUri.fsPath}`);
    });
  } else {
    console.log('Git API is not available');
  }

  const HELLO_WORLD_COMMAND = 'my-extension.helloWorld';
  const helloWorldDisposable = vscode.commands.registerCommand(HELLO_WORLD_COMMAND, () => {
    vscode.window.showInformationMessage('Hello World from my extension!');
  });

  const LIST_BRANCHES_COMMAND = 'my-extension.listBranches';
  const listBranchesDisposable = vscode.commands.registerCommand(LIST_BRANCHES_COMMAND, () => {
    if (gitExtension) {
      const { repositories } = gitExtension;
      repositories.forEach((repo: any) => {
        const branches = repo.state.refs.filter((ref: any) => ref.type === 0); // 0 is RefType.Head
        branches.forEach((branch: any) => {
          vscode.window.showInformationMessage(`Branch: ${branch.name}`);
        });
      });
    } else {
      vscode.window.showInformationMessage('Git API is not available');
    }
  });

  const COMMIT_CHANGES_COMMAND = 'my-extension.commitChanges';
  const commitChangesDisposable = vscode.commands.registerCommand(COMMIT_CHANGES_COMMAND, async () => {
    if (gitExtension) {
      const { repositories } = gitExtension;
      repositories.forEach(async (repo: any) => {
        try {
          await repo.inputBox.commit();
          vscode.window.showInformationMessage('Changes committed');
        } catch (error) {
          if (error instanceof Error) {
            vscode.window.showErrorMessage(`Failed to commit changes: ${error.message}`);
          } else {
            vscode.window.showErrorMessage('Failed to commit changes: Unknown error');
          }
        }
      });
    } else {
      vscode.window.showInformationMessage('Git API is not available');
    }
  });

  context.subscriptions.push(helloWorldDisposable, listBranchesDisposable, commitChangesDisposable);
}

export function deactivate() {}
