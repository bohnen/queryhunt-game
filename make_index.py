#!/bin/env python
# -*- coding: utf-8 -*-
# Make index from schema file

import os

import streamlit as st
from llama_index.core import (SimpleDirectoryReader, StorageContext,
                              VectorStoreIndex)
from llama_index.core.vector_stores.types import (MetadataFilter,
                                                  MetadataFilters)
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.tidbvector import TiDBVectorStore

vs_table_name = "vs_game_schema"
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

tidbvec = TiDBVectorStore(
    connection_string=st.secrets["TIDB_CONNECTION_URL"],
    table_name=vs_table_name,
    distance_strategy="cosine",
    vector_dimension=1536,
    drop_existing_table=True,
)

documents = SimpleDirectoryReader("./data").load_data()
for doc in documents:
    doc.metadata["schema"] = "sql_mystery_game"
    
try:
    storage_context = StorageContext.from_defaults(vector_store=tidbvec)
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, show_progress=True
    )
except Exception as e:
    print(f"Error: {e}")

print("Indexing complete")