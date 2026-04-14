import pandas as pd

class AirbnbRemoteData:

    def __init__(self, url_a: str, url_b: str):
        self.url_a = url_a
        self.url_b = url_b
        self.df_a_columns = None
        self.df_b_columns = None
        self.df_a = None
        self.df_b = None

    def fetch_data(self):
        if self.df_a is None or self.df_b is None:
            try:
                self.df_a = pd.read_csv(self.url_a)
                self.df_a['city'] = 'Berlin'
                self.df_b = pd.read_csv(self.url_b)
                self.df_b['city'] = 'Munich'
                self.df_a_columns = self.df_a.columns
                self.df_b_columns = self.df_b.columns
            except Exception as e:
                print(f"Error downloading or parsing CSV: {e}")
                raise

    def get_berlin_data_frame_columns(self) -> pd.Index:
        return self.df_a.columns

    def get_munich_data_frame_columns(self) -> pd.Index:
        return self.df_b.columns

    def get_combined_data(self) -> pd.DataFrame:
        try:
            return pd.concat([self.df_a, self.df_b], axis=0, ignore_index=True)
        except Exception as e:
            print(f"Error merging dataframes: {e}")
            return None