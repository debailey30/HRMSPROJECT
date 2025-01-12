export interface GitExtension {
    readonly enabled: boolean;
    readonly onDidChangeEnablement: Event<boolean>;
    readonly repositories: Repository[];
    getAPI(): API;
}

export interface Repository {
    readonly rootUri: Uri;
    readonly inputBox: InputBox;
    readonly state: RepositoryState;
    readonly ui: RepositoryUIState;
    readonly onDidChangeRepository: Event<void>;
    readonly onDidChangeState: Event<void>;
    readonly onDidChangeUiState: Event<void>;
    getConfigs(): Promise<{ key: string; value: string }[]>;
    getConfig(key: string): Promise<string>;
    setConfig(key: string, value: string): Promise<string>;
    getGlobalConfig(key: string): Promise<string>;
    getObjectDetails(treeish: string, path: string): Promise<GitObject>;
    detectObjectType(object: string): Promise<{ mimetype: string; encoding?: string }>;
    buffer(ref: string, path: string): Promise<Buffer>;
    show(ref: string, path: string): Promise<string>;
    getCommit(ref: string): Promise<Commit>;
    add(paths: string[]): Promise<void>;
    rm(paths: string[]): Promise<void>;
    stage(path: string, data: string): Promise<void>;
    commit(message: string, opts?: CommitOptions): Promise<void>;
    clean(paths: string[]): Promise<void> {
        // Use the paths parameter to avoid the unused variable error
        console.log(`Cleaning paths: ${paths.join(', ')}`);
        return Promise.resolve();
    }
    clean(paths: string[]): Promise<void>;
    pull(): Promise<void>;
    push(): Promise<void>;
}

export interface API {
    readonly repositories: Repository[];
    getRepository(): Repository | null;
    init(root: Uri): Promise<Repository | null>;
    openRepository(root: Uri): Promise<Repository | null>;
}

export interface InputBox {
    value: string;
}

export interface RepositoryState {
    readonly HEAD: Branch | undefined;
    readonly refs: Ref[];
    readonly remotes: Remote[];
    readonly submodules: Submodule[];
    readonly rebaseCommit: Commit | undefined;
    readonly mergeChanges: Change[];
    readonly indexChanges: Change[];
    readonly workingTreeChanges: Change[];
    readonly onDidChange: Event<void>;
}

export interface RepositoryUIState {
    readonly selected: boolean;
    readonly onDidChange: Event<void>;
}

export interface CommitOptions {
    all?: boolean | 'tracked';
    amend?: boolean;
    signoff?: boolean;
    signCommit?: boolean;
    empty?: boolean;
    noVerify?: boolean;
    requireUserConfig?: boolean;
}

export interface GitObject {
    readonly type: string;
    readonly object: string;
    readonly size: number;
}

export interface Commit {
    readonly hash: string;
    readonly message: string;
    readonly parents: string[];
    readonly authorDate: Date;
    readonly authorName: string;
    readonly authorEmail: string;
    readonly commitDate: Date;
}

export interface Branch extends Ref {
    readonly upstream?: Branch;
    readonly ahead?: number;
    readonly behind?: number;
}

export interface Ref {
    readonly type: RefType;
    readonly name?: string;
    readonly commit?: string;
    readonly remote?: string;
}

export enum RefType {
    Head,
    RemoteHead,
    Tag
}

export interface Remote {
    readonly name: string;
    readonly fetchUrl: string;
    readonly pushUrl?: string;
    readonly isReadOnly: boolean;
}

export interface Submodule {
    readonly name: string;
    readonly path: string;
    readonly url: string;
}

export interface Change {
    readonly uri: Uri;
    readonly originalUri: Uri;
    readonly renameUri: Uri | undefined;
    readonly status: ChangeStatus;
}

export enum ChangeStatus {
    INDEX_MODIFIED,
    INDEX_ADDED,
    INDEX_DELETED,
    MODIFIED,
    DELETED,
    UNTRACKED,
    IGNORED,
    INTENT_TO_ADD,
    ADDED_BY_US,
    ADDED_BY_THEM,
    DELETED_BY_US,
    DELETED_BY_THEM,
    BOTH_ADDED,
    BOTH_DELETED,
    BOTH_MODIFIED
}

export interface Uri {
    readonly scheme: string;
    readonly authority: string;
    readonly path: string;
    readonly query: string;
    readonly fragment: string;
    readonly fsPath: string;
    with(change: { scheme?: string; authority?: string; path?: string; query?:
    string; fragment?: string }): Uri;
    toString(skipEncoding?: boolean): string;
    toJSON(): any;
}

export interface Event<T> {
    (listener: (e: T) => any, thisArgs?: any, disposables?: any[]): Disposable;
}

export interface API {
    readonly repositories: Repository[];
    toGitUri(uri: Uri, ref: string): Uri;
    getRepository(): Repository | null;
    init(root: Uri): Promise<Repository | null>;
    openRepository(root: Uri): Promise<Repository | null>;
}

export interface Disposable {
    dispose(): void;
}
