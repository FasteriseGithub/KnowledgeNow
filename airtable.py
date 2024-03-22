from pyairtable import Api

#airtable_key = 'pato8cChB3wsNWWyG.c8cea7e3657770665e0400a6dfd1819c9ebe01e606688294152e78f190e9a2a7'
#airtable_api = Api(airtable_key)

#base_id = 'app4ngdBC3uyeutjO'
#icebreakers_table_name = 'Ice_Breakers'


class AirTable:
    """
    Class to handle Airtable API data uploads

    Args:
        airtable_api_key (str): The Airtable API key (obtain through AirTable settings).
        base_id (str): The ID of the base in Airtable (the first code after airtable.com/BASE_ID/...). Eg, in https://airtable.com/app4ngdBC3uyeutjO/tbl6TmlXJj90bOFaZ/ , the base ID is 'app4ngdBC3uyeutjO'.
        table_name (str): The name of the table in Airtable (not the id, just the name).
    """
    airtable_api_key = 'pat0aBSKUoSeUHC8b.093ccf2cd043adffcbecd3b03d18a52c71dfdf92fe5c06dc1e5b169cbd0a89a9'
    base_id = 'appFJEwA3C5AynRXI'
    table_name = 'KnowledgeNowMVP'

    def __init__(self, airtable_api_key=airtable_api_key, base_id=base_id, table_name=table_name):
        self.airtable_api_key = airtable_api_key
        self.base_id = base_id
        self.table_name = table_name
        self.api = Api(self.airtable_api_key) 
        self.table = self.api.table(self.base_id, self.table_name)

        print("""
        To post data to the Airtable table.
        Args:
            data (dict): A dictionary with the format `{'column_name': data_to_post, ...}`.
        
        Keys for dictionary:
              {
                name_of_dev: "",
                model_name: "",
                human_prompt: "",
                global_context: "",
                context_entrichment_agent_system_prompt: "",
                enriched_prompt_output: "",
                rag_extractor_agent_system_prompt: "",
                rag_optimized_queries_output: "",
                total_chunks_retrieved: "",
                chunk_size: "",
                knowledge_base_docs_list: "",
                evaluator_agent_system_prompt: "",
                reranked_rag_queries_output: "",
                answer_agent_system_prompt: "",
                final_answer_to_user: ""
              }
        """)

    def post_data_to_table(self, data:dict):
        """
        Posts data to the Airtable table.
        Args:
            data (dict): A dictionary with the format `{'column_name': data_to_post, ...}`.
        """
        #print(self.post_data_to_table.__doc__)


        try:
            self.table.create(data)
            print("data posted to Airtable successfully.")
        except Exception as e:
            print(f"Error posting to Airtable: {e}")

airtable = AirTable()
airtable.post_data_to_table(data={'name_of_dev': "Alejo_Fastest"})