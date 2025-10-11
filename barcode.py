import datetime
import logging
import sys
import os

# 로깅 설정
def setup_logging():
    """로그 파일 및 콘솔 출력 설정"""
    os.makedirs("barcode_logs", exist_ok=True)
    log_file = f"barcode_logs/barcode_{datetime.datetime.now().strftime('%Y%m%d')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

def main():
    """바코드 스캐너 프로그램"""
    logger = setup_logging()
    
    print("="*50)
    print("MIRACLEM MQ150 바코드 스캐너")
    print("="*50)
    print("바코드를 스캔하세요. (종료: 'exit' 입력 또는 Ctrl+C)")
    print("-"*50)
    
    scan_count = 0
    
    try:
        while True:
            barcode = input("\n바코드 대기 중: ").strip()
            
            if barcode.lower() == 'exit':
                break
            
            if not barcode:
                continue
            
            scan_count += 1
            timestamp = datetime.datetime.now()
            
            # 로그 기록
            logger.info(f"Scan #{scan_count} | Barcode: {barcode} | Length: {len(barcode)}")
            
            # 화면 출력
            print(f"\n[스캔 성공]")
            print(f"  시간: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  번호: #{scan_count}")
            print(f"  바코드: {barcode}")
            print(f"  길이: {len(barcode)}자")
            print("-"*50)
            
    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다.")
    except Exception as e:
        logger.error(f"오류 발생: {str(e)}")
        print(f"\n오류 발생: {str(e)}")
    finally:
        print(f"\n총 {scan_count}개의 바코드를 스캔했습니다.")
        logger.info(f"프로그램 종료 - 총 스캔 수: {scan_count}")

if __name__ == "__main__":
    main()