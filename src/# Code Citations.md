# Code Citations

## License: MIT

[LiveCode Test MockVscode](https://github.com/Xirider/LiveCode/tree/eb677fc786f6ff0c3a308ae464487681fa2f9be9/test/mockVscode.spec.ts)

```typescript
TextLine;
           lineAt(position: Position): TextLine;
           offsetAt(position: Position): number;
           positionAt(offset: number): Position;
           getText(range?: Range): string;
           getWordRangeAtPosition(position: Position, regex?: RegExp): Range | undefined;
```

## License: Apache_2_0 (Test Interfaces 08)

[TS2Python Test Interfaces](https://github.com/jecki/ts2python/tree/aa30c91741ea9117a46883b2de9ab91cd02f61a6/tests_grammar/08_test_Interfaces.ini)

```typescript
Uri;
           readonly fileName: string;
           readonly isUntitled: boolean;
           readonly languageId: string;
           readonly version: number;
           readonly isDirty: boolean;
           readonly isClosed: boolean;
           save(): Thenable<boolean>;
           readonly eol: EndOfLine;
           readonly lineCount: number;
           lineAt(line:
```

## License: Apache_2_0 (Test Interfaces 07)

[TS2Python Test Interfaces](https://github.com/jecki/ts2python/tree/aa30c91741ea9117a46883b2de9ab91cd02f61a6/tests_grammar/07_test_Interfaces.ini)

```typescript
;
           readonly languageId: string;
           readonly version: number;
           readonly isDirty: boolean;
           readonly isClosed: boolean;
           save(): Thenable<boolean>;
           readonly eol: EndOfLine;
           readonly lineCount: number;
           lineAt(line: number): TextLine;
           lineAt(position: Position)
```

## License: unknown

[Webpack Monaco ExtHostTypes](https://github.com/rebornix/webpack-monaco/tree/87c52f7b0625cfd980b2f62cb8c3553c1bea61b1/vscode/workbench/api/node/extHostTypes.d.ts)

```typescript
line: number;
           readonly character: number;
           constructor(line: number, character: number);
           isBefore(other: Position): boolean;
           isBeforeOrEqual(other: Position): boolean;
           isAfter(other: Position): boolean;
           isAfterOrEqual(other: Position): boolean
```

## License: Apache_2_0 (Test Playground)

[TS2Python Test Playground](https://github.com/jecki/ts2python/tree/aa30c91741ea9117a46883b2de9ab91cd02f61a6/tests_grammar/99_test_Playground.ini)

```typescript
class Position {
           readonly line: number;
           readonly character: number;
           constructor(line: number, character: number);
           isBefore(other: Position): boolean;
           isBeforeOrEqual(other: Position): boolean;
           isAfter(other: Position): boolean;
           isAfterOrEqual(other:
