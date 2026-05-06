from ingest.language_detector import detect_language
    def _traverse_tree(
        self,
        node,
        code,
        language,
        file_path,
        chunks
    ):

        function_nodes = FUNCTION_NODES.get(language, [])
        class_nodes = CLASS_NODES.get(language, [])

        if node.type in function_nodes:

            chunks.append(
                self._create_chunk(
                    node,
                    code,
                    language,
                    file_path,
                    "function"
                )
            )

        elif node.type in class_nodes:

            chunks.append(
                self._create_chunk(
                    node,
                    code,
                    language,
                    file_path,
                    "class"
                )
            )

        for child in node.children:
            self._traverse_tree(
                child,
                code,
                language,
                file_path,
                chunks
            )

    def _create_chunk(
        self,
        node,
        code,
        language,
        file_path,
        chunk_type
    ):

        start_byte = node.start_byte
        end_byte = node.end_byte

        chunk_content = code[start_byte:end_byte]

        chunk = {
            "content": chunk_content,
            "type": chunk_type,
            "language": language,
            "filepath": file_path,
            "start_line": node.start_point[0] + 1,
            "end_line": node.end_point[0] + 1
        }

        return chunk