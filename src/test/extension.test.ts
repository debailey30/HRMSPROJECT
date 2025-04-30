import * as assert from 'assert';
import * as vscode from 'vscode';
import * as myExtension from '../../src/extension';

suite('Extension Test Suite', () => {
	vscode.window.showInformationMessage('Start all tests.');

	test('Sample test', () => {
		assert.strictEqual(-1, [1, 2, 3].indexOf(5));
		assert.strictEqual(-1, [1, 2, 3].indexOf(0));
	});

	suite('Extension Activation', () => {
		test('should activate the extension', async () => {
			const extension = vscode.extensions.getExtension('my-extension');
			if (!extension) {
				assert.fail('Extension not found');
			}
			await extension?.activate();
			assert.ok(extension?.isActive);
		});

		test('should register helloWorld command', async () => {
			const commands = await vscode.commands.getCommands(true);
			assert.ok(commands.includes('my-extension.helloWorld'));
		});
	});

	suite('Hello World Command', () => {
		test('should display Hello World message', async () => {
			const showInformationMessageStub = sinon.stub(vscode.window, 'showInformationMessage');
			await vscode.commands.executeCommand('my-extension.helloWorld');
			assert.ok(showInformationMessageStub.calledOnceWith('Hello World from my_extension!'));
			showInformationMessageStub.restore();
		});
	});
});
