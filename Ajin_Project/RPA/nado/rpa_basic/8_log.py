# import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s [%(levelname)s] %(message)s")

# # debug < info < waring < error < critical

# logging.debug("아 이거 누가짬?")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래 되었습니다.")
# logging.error("에러 발생. 에러코드는...")
# logging.critical("복구 불가능한 심각한 문제 발생")

# 터미널과 파일에 함꼐 로그 남기기
import logging
from datetime import datetime
# 시간 [로그레벨] 메시지 형태로 로그 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")
