# number of session - YYMMDD_hhmmss

# 1 - 130212_141126

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130212_141126_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130212_141126_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130212_141126_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130212_141126_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130212_141126_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130212_141126_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130212_141126_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130212_141126_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';


# 2 - 130312_182133

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130312_182133_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130312_182133_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130312_182133_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130312_182133_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130312_182133_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130312_182133_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130312_182133_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130312_182133_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';


# 3 - 130313_040959

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130313_040959_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_040959_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130313_040959_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_040959_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130313_040959_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_040959_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130313_040959_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_040959_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 4 - 130313_075802

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130313_075802_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_075802_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130313_075802_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_075802_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130313_075802_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_075802_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130313_075802_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_075802_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 5 - 130313_091514

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130313_091514_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_091514_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130313_091514_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_091514_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130313_091514_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_091514_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130313_091514_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_091514_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 6 - 130313_172309

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130313_172309_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_172309_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130313_172309_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_172309_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130313_172309_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_172309_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130313_172309_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_172309_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 7 - 130313_182111

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130313_182111_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_182111_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130313_182111_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_182111_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130313_182111_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_182111_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130313_182111_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_182111_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 8 - 130313_193632

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130313_193632_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_193632_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130313_193632_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_193632_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130313_193632_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_193632_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130313_193632_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130313_193632_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 9 - 130316_091951

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130316_091951_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130316_091951_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130316_091951_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130316_091951_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130316_091951_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130316_091951_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130316_091951_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130316_091951_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 10 - 130422_080447

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130422_080447_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130422_080447_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130422_080447_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130422_080447_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130422_080447_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130422_080447_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130422_080447_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130422_080447_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 11 - 130423_085134

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 130423_085134_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130423_085134_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 130423_085134_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130423_085134_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 130423_085134_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130423_085134_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 130423_085134_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/130423_085134_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 12 - 131111_071927

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131111_071927_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_071927_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131111_071927_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_071927_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131111_071927_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_071927_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131111_071927_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_071927_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 13 - 131111_073513

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131111_073513_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_073513_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131111_073513_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_073513_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131111_073513_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_073513_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131111_073513_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131111_073513_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 14 - 131113_054328

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131113_054328_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054328_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131113_054328_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054328_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131113_054328_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054328_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131113_054328_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054328_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 15 - 131113_054733

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131113_054733_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054733_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131113_054733_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054733_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131113_054733_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054733_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131113_054733_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_054733_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 16 - 131113_072857

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131113_072857_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_072857_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131113_072857_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_072857_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131113_072857_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_072857_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131113_072857_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131113_072857_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 17 - 131114_053435

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131114_053435_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131114_053435_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131114_053435_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131114_053435_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131114_053435_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131114_053435_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131114_053435_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131114_053435_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 18 - 131118_140809

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131118_140809_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_140809_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131118_140809_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_140809_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131118_140809_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_140809_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131118_140809_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_140809_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 19 - 131118_143720

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131118_143720_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_143720_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131118_143720_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_143720_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131118_143720_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_143720_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131118_143720_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131118_143720_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 20 - 131121_083431

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131121_083431_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131121_083431_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131121_083431_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131121_083431_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131121_083431_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131121_083431_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131121_083431_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131121_083431_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 21 - 131128_084046

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 131128_084046_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131128_084046_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 131128_084046_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131128_084046_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 131128_084046_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131128_084046_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 131128_084046_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/131128_084046_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 22 - 140128_072312

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140128_072312_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_072312_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140128_072312_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_072312_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140128_072312_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_072312_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140128_072312_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_072312_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 23 - 140128_104551

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140128_104551_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_104551_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140128_104551_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_104551_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140128_104551_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_104551_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140128_104551_NetworkEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140128_104551_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 24 - 140129_030740

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140129_030740_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140129_030740_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140129_030740_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140129_030740_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140129_030740_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140129_030740_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140129_030740_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140129_030740_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 25 - 140130_080727

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140130_080727_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_080727_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140130_080727_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_080727_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140130_080727_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_080727_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140130_080727_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_080727_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 26 - 140130_083503

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140130_083503_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_083503_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140130_083503_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_083503_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140130_083503_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_083503_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140130_083503_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140130_083503_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 27 - 140201_091930

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140201_091930_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_091930_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140201_091930_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_091930_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140201_091930_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_091930_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140201_091930_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_091930_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 28 - 140201_100133

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140201_100133_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_100133_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140201_100133_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_100133_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140201_100133_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_100133_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140201_100133_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140201_100133_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 29 - 140208_091407

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_091407_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_091407_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_091407_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_091407_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_091407_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_091407_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_091407_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_091407_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 30 - 140208_092732

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_092732_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_092732_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_092732_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_092732_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_092732_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_092732_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_092732_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_092732_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 31 - 140208_093259

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_093259_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093259_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_093259_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093259_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_093259_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093259_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_093259_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093259_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 32 - 140208_093418

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_093418_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093418_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_093418_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093418_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_093418_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093418_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_093418_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093418_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 33 - 140208_093959

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_093959_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093959_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_093959_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093959_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_093959_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093959_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_093959_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_093959_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 34 - 140208_095202

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_095202_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_095202_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_095202_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_095202_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_095202_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_095202_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_095202_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_095202_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 35 - 140208_114412

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_114412_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_114412_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_114412_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_114412_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_114412_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_114412_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_114412_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_114412_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 36 - 140208_115932

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140208_115932_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_115932_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140208_115932_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_115932_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140208_115932_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_115932_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140208_115932_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140208_115932_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 37 - 140211_181958

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140211_181958_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_181958_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140211_181958_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_181958_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140211_181958_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_181958_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140211_181958_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_181958_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 38 - 140211_184316

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140211_184316_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_184316_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140211_184316_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_184316_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140211_184316_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_184316_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140211_184316_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140211_184316_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 39 - 140212_181933

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140212_181933_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_181933_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140212_181933_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_181933_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140212_181933_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_181933_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140212_181933_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_181933_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 40 - 140212_183902

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140212_183902_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_183902_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140212_183902_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_183902_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140212_183902_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_183902_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140212_183902_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140212_183902_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 41 - 140218_181920

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140218_181920_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_181920_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140218_181920_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_181920_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140218_181920_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_181920_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140218_181920_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_181920_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

# 42 - 140218_183803

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName
FROM 140218_183803_AvatarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_183803_avatar.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, LPositionX, LPositionY, LPositionZ, LRotationY, LPlayerName,
	   LSpeed, LBrakeInput, LAccInput
FROM 140218_183803_CarEntity
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_183803_car.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT DISTINCT Sender
FROM 140218_183803_ChatMessageEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_183803_message.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

SELECT LTimeStamp, Type, Arg
FROM 140218_183803_LogEvent
INTO OUTFILE '/home/dan/Bureau/csv_everscape/140218_183803_log.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';

