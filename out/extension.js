"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
function activate(context) {
    var _a;
    const gitExtension = (_a = vscode.extensions.getExtension('vscode.git')) === null || _a === void 0 ? void 0 : _a.exports.getAPI(1);
    if (gitExtension) {
        const { repositories } = gitExtension;
        repositories.forEach((repo) => {
            console.log(`Repository: ${repo.rootUri.fsPath}`);
        });
    }
    else {
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
            repositories.forEach((repo) => {
                const branches = repo.state.refs.filter((ref) => ref.type === 0); // 0 is RefType.Head
                branches.forEach((branch) => {
                    vscode.window.showInformationMessage(`Branch: ${branch.name}`);
                });
            });
        }
        else {
            vscode.window.showInformationMessage('Git API is not available');
        }
    });
    const COMMIT_CHANGES_COMMAND = 'my-extension.commitChanges';
    const commitChangesDisposable = vscode.commands.registerCommand(COMMIT_CHANGES_COMMAND, () => __awaiter(this, void 0, void 0, function* () {
        if (gitExtension) {
            const { repositories } = gitExtension;
            repositories.forEach((repo) => __awaiter(this, void 0, void 0, function* () {
                try {
                    yield repo.inputBox.commit();
                    vscode.window.showInformationMessage('Changes committed');
                }
                catch (error) {
                    if (error instanceof Error) {
                        vscode.window.showErrorMessage(`Failed to commit changes: ${error.message}`);
                    }
                    else {
                        vscode.window.showErrorMessage('Failed to commit changes: Unknown error');
                    }
                }
            }));
        }
        else {
            vscode.window.showInformationMessage('Git API is not available');
        }
    }));
    context.subscriptions.push(helloWorldDisposable, listBranchesDisposable, commitChangesDisposable);
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map