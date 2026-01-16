from cite_exchange import CexBlock
import logging

class HmtArchive():
    """
    A class represent a published release of the Homer Multitext project archive.

    Attributes:
        blocks (str): The full contents of a published release of the Homer Multitext project archive, parsed into labelled blocks of delimited-text data.
    """
    blocks: List[CexBlock]

    def __init__(self):
        current_url = "https://raw.githubusercontent.com/homermultitext/hmt-archive/refs/heads/master/releases-cex/hmt-current.cex" 
        logging.info("Downloading archive...")
        all_blocks = CexBlock.from_url(current_url)
        logging.info("Download complete.")
        self.blocks = all_blocks