# Code Citations

## License: MIT (Repository 1)

[https://github.com/microsoft/vscode-azurestaticwebapps/tree/802cbb0c8a3d345c27ad393f45bdad66224e7a66/src/git.d.ts](https://github.com/microsoft/vscode-azurestaticwebapps/tree/802cbb0c8a3d345c27ad393f45bdad66224e7a66/src/git.d.ts)

```typescript
repositories: Repository[];
toGitUri(uri: Uri, ref: string): Uri;
getRepository(uri: Uri): Repository | null;
init(root: Uri): Promise<Repository | null>;
openRepository(root: Uri): Promise<Repository | null> {
  // method implementation
}
```typescript
```plaintext

init(root: Uri): Promise<Repository | null>;
open-repository(root: Uri): Promise<Repository | null>;

```typescript
getConfig(key: string): Promise<{ key: string; value: string }[]>;
```plaintext

setConfig(key: string, value: string): Promise<string>;
`getGlobalConfig(key: string): Promise<string>;`
getObjectDetails(ref: string, path: string): Promise<{ mode: number; object: string; oid: string }>;

```plaintext

getObjectDetails
```plaintext

## License: MIT

[https://github.com/DonJayamanne/test_gitHistory/tree/f026e09cbe793c042d39153becb9c4553a25d83b/src/adapter/repository/git.d.ts](https://github.com/DonJayamanne/test_gitHistory/tree/f026e09cbe793c042d39153becb9c4553a25d83b/src/adapter/repository/git.d.ts)

```typescript
(): Promise<{ key: string; value: string }[]>;
getGlobalConfig(key: string): Promise<string>;
setConfig(key: string, value: string): Promise<string>;
getGlobalConfig(key: string): Promise<string>;
```plaintext

```plaintext

<https://github.com/BearLee2/teste/tree/87a654edf311c9ce7a02ecb667944fea830b08b6/vscode-main/extensions/github/src/typings/git.d.ts>
`Promise<string>;`

```typescript
string }>;
buffer(ref: string, path: string): Promise<Buffer>;
show(ref: string, path: string): Promise<string>;
getCommit(ref: string): Promise<Commit>;
add(paths: string[]): Promise<void>;
```plaintext

```plaintext

```typescript
: Branch | undefined;
```typescript
: Branch | undefined;
readonly refs: Ref[];
readonly remotes: Remote[];
readonly submodules: Submodule[];
readonly rebaseCommit: Commit | undefined;
readonly mergeChanges: Change[];
readonly indexChanges: Change[];
readonly workingTreeChanges: Change[];
```plaintext

readonly submodules: Submodule[];
readonly rebaseCommit: Commit | undefined;
readonly mergeChanges: Change[];
readonly indexChanges: Change[];
readonly workingTreeChanges: Change[];
`
plaintext
init(root: Uri): Promise<Repository | null>;
open-repository(root: Uri): Promise<Repository | null>;

    text=auto
    text eol=lf


## Ensure all files use LF line endings

* text eol=lf

## Specific files can have different settings

*.bat text eol=crlf
*.sh text eol=lf
