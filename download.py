from pathlib import Path

from tqdm import tqdm
import asyncio
import aiohttp


async def download_file(url: str):
    data_path = Path(__file__).parent / 'data'
    file_name = data_path / url.split('/')[-1]
    print(f'Downloading {url} to {file_name}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                file_size = int(resp.headers['Content-Length'])
                with open(file_name, 'wb') as fd:
                    with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
                        while True:
                            chunk = await resp.content.read(1024)
                            if not chunk:
                                break
                            fd.write(chunk)
                            pbar.update(len(chunk))
            else:
                print("Failed to download the file.")


if __name__ == '__main__':
    urls = [
        "https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Field-of-Study_09262023.zip",
        "https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Institution_09262023.zip",
        "https://ed-public-download.app.cloud.gov/downloads/CollegeScorecard_Raw_Data_09262023.zip",
        "https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Field-of-Study_09262023.zip",
        "https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Institution_09262023.zip",
        "https://ed-public-download.app.cloud.gov/downloads/CollegeScorecard_Raw_Data_09262023.zip",
        "https://data.opensanctions.org/datasets/20240430/default/entities.ftm.json",
        "https://data.opensanctions.org/datasets/20240430/default/topics.nested.json",
        "https://data.opensanctions.org/datasets/20240430/default/targets.simple.csv",
        "https://data.opensanctions.org/datasets/20240430/default/targets.nested.json",
        "https://data.opensanctions.org/datasets/20240430/default/statistics.json",
        "https://data.opensanctions.org/datasets/20240430/default/statements.csv",
        "https://data.opensanctions.org/datasets/20240430/default/senzing.json",
        "https://data.opensanctions.org/datasets/20240430/default/names.txt"
    ]
    for url in urls:
        asyncio.run(download_file(url))
