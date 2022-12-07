from __future__ import annotations

from rich import print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def riddle1(riddle_input: str) -> int | str:
    root = build_filesystem(riddle_input)
    answer = root.add_size_of_folders_below_size()
    return answer


def riddle2(riddle_input: str) -> int | str:
    root = build_filesystem(riddle_input)
    used_space = root.get_size()
    total_space = 70000000
    free_space = total_space - used_space
    required = 30000000
    space_to_free = required - free_space
    answer = root.free_up_space(space_to_free, used_space)
    return answer


def build_filesystem(riddle_input: str) -> Folder:
    filesystem = Folder("/")
    current_folder = filesystem
    for line in riddle_input.splitlines()[1:]:
        if line.startswith("$ cd"):
            current_folder = current_folder.cd_folder(line.split(" ")[-1])
        elif line.startswith("$ ls"):
            # do nothing
            continue
        elif line.startswith("dir"):
            current_folder.add_dir(line.split(" ")[-1])
        else:  # file with size
            filesize = int(line.split(" ")[0])
            filename = line.split(" ")[-1]
            current_folder.add_file(filename, filesize)

    root = filesystem.go_to_top()
    return root


class File:
    def __init__(self, name: str, size: int, parent: Folder):
        self.name = name
        self.size = size
        self.parent: Folder = parent


class Folder:
    def __init__(self, name: str, parent: Folder | None = None):
        self.name = name
        self.files: list[File] = []
        self.subfolder: list[Folder] = []
        self.parent: Folder = parent if parent else self

    def free_up_space(self, space_needed: int, current_strategy: int) -> int:
        if (s := self.get_size()) > space_needed:
            # valid strategy, but not necessarily best
            if s < current_strategy:
                current_strategy = s
        for folder in self.subfolder:
            current_strategy = folder.free_up_space(space_needed, current_strategy)
        return current_strategy

    def print(self, indent: str = "") -> None:
        if self.parent == self:
            print(f"  {self.name} (dir,size={self.get_size()})")
            print("  \\")
        else:
            print(f"{indent} |-{self.name} (dir,size={self.get_size()})")
            print(f"{indent}  \\")
        for file in self.files:
            print(f"{indent}   |-{file.name} (file,size={file.size})")
        for folder in self.subfolder:
            folder.print(indent=indent + "  ")

    def add_size_of_folders_below_size(self, count: int = 0, threshold=100000) -> int:
        if (s := self.get_size()) < threshold:
            count += s
        for folder in self.subfolder:
            count += folder.add_size_of_folders_below_size(threshold=threshold)

        return count

    def get_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.size
        for folder in self.subfolder:
            size += folder.get_size()
        return size

    def go_to_top(self) -> Folder:
        if self.parent == self:
            return self
        else:
            return self.parent.go_to_top()

    def add_file(self, name: str, size: int) -> None:
        for file in self.files:
            if name == file.name:
                break
        else:
            new_file = File(name, size, self)
            self.files.append(new_file)

    def add_dir(self, name: str) -> None:
        for folder in self.subfolder:
            if name == folder.name:
                break
        else:
            new_folder = Folder(name, self)
            self.subfolder.append(new_folder)

    def cd_parent(self) -> Folder:
        return self.parent

    def cd_folder(self, name: str) -> Folder:
        if name == "..":
            return self.cd_parent()
        else:
            for folder in self.subfolder:
                if folder.name == name:
                    return folder
            new_folder = Folder(name, self)
            self.subfolder.append(new_folder)
            return new_folder


if __name__ == "__main__":
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)
    answer1 = riddle1(riddle_input)
    print(answer1)

    answer2 = riddle2(riddle_input)
    print(answer2)
