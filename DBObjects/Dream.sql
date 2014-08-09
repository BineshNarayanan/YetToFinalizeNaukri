CREATE TABLE Applications (
  Id REAL NOT NULL AUTO_INCREMENT,
  Seeker_Id REAL NOT NULL,
  Posts_Id REAL NOT NULL,
  ApplicationDate DATE NULL,
  IsViewed BIT NULL,
  CreateDate DATE NULL,
  ViewedDate DATE NULL,
  PRIMARY KEY(Id),
  INDEX Applications_FKIndex1(Posts_Id),
  INDEX Applications_FKIndex2(Seeker_Id)
);


CREATE TABLE IndustryGroupMaster (
  Id REAL NOT NULL AUTO_INCREMENT,
  IndustrySectorMaster_Id REAL NOT NULL,
  GroupCode REAL NULL,
  GroupName VARCHAR(100) NULL,
  PRIMARY KEY(Id),
  INDEX IndustryGroupMaster_FKIndex1(IndustrySectorMaster_Id)
);


CREATE TABLE IndustryMaster (
  Id REAL NOT NULL AUTO_INCREMENT,
  IndustryGroupMaster_Id REAL NOT NULL,
  IndustryCode REAL NULL,
  IndustryName VARCHAR(200) NULL,
  IndustryDescription VARCHAR(500) NULL,
  PRIMARY KEY(Id),
  INDEX IndustryMaster_FKIndex1(IndustryGroupMaster_Id)
);


CREATE TABLE IndustrySectorMaster (
  Id REAL NOT NULL AUTO_INCREMENT,
  SectorCode REAL NULL,
  SectorName VARCHAR(50) NULL,
  PRIMARY KEY(Id)
);


CREATE TABLE Posts (
  Id REAL NOT NULL AUTO_INCREMENT,
  ProviderGroup_Id REAL NOT NULL,
  Title VARCHAR(200) NOT NULL,
  Description INTEGER NOT NULL,
  CreationDate DATE NULL,
  Domain VARCHAR(50) NULL,
  PostViewCount REAL NULL,
  ApplicationCount REAL NULL,
  SkillSetsRequired VARCHAR(1000) NULL,
  PRIMARY KEY(Id),
  INDEX Posts_FKIndex1(ProviderGroup_Id)
);


CREATE TABLE PostViewStats (
  Id REAL NOT NULL AUTO_INCREMENT,
  Posts_Id REAL NOT NULL,
  PostViewedOn DATE NULL,
  PostViewedBy REAL NULL,
  PRIMARY KEY(Id),
  INDEX PostViewStats_FKIndex1(Posts_Id)
);


CREATE TABLE ProfileViewStats (
  Id REAL NOT NULL AUTO_INCREMENT,
  Seeker_Id REAL NOT NULL,
  ProfileViewedOn DATE NULL,
  ViewedBy REAL NULL,
  PRIMARY KEY(Id),
  INDEX ProfileViewStats_FKIndex1(Seeker_Id)
);


CREATE TABLE Provider (
  Id REAL NOT NULL AUTO_INCREMENT,
  ProviderGroup_Id REAL NOT NULL,
  Name VARCHAR(100) NULL,
  ProviderType VARCHAR(20) NULL,
  RegistrationDate DATE NULL,
  CreateDate DATE NULL,
  UpdateDate DATE NULL,
  IsActive BIT NULL,
  PrimaryEmail VARCHAR(100) NULL,
  SecondaryEmail VARCHAR(100) NULL,
  PRIMARY KEY(Id),
  INDEX Provider_FKIndex1(ProviderGroup_Id)
);


CREATE TABLE ProviderGroup (
  Id REAL NOT NULL AUTO_INCREMENT,
  Name VARCHAR(200) NULL,
  ProviderType VARCHAR(100) NULL,
  CreateDate DATE NULL,
  CreatedBy REAL NULL,
  UpdateDate DATE NULL,
  UpdatedBy REAL NULL,
  IsActive BIT NULL,
  PrimaryEmail VARCHAR(100) NULL,
  SecondaryEmail VARCHAR(100) NULL,
  PRIMARY KEY(Id)
);


CREATE TABLE ProviderSubscriptionDetails (
  Id REAL NOT NULL AUTO_INCREMENT,
  ProviderGroup_Id REAL NOT NULL,
  SubscriptionMaster_Id REAL NOT NULL,
  SubscriptionStartDate DATE NULL,
  SubscriptionEndDate DATE NULL,
  IsActive BIT NULL,
  CreateDate DATE NULL,
  CreatedBy VARCHAR(20) NULL,
  UpdateDate DATE NULL,
  UpdatedBy VARCHAR(20) NULL,
  PRIMARY KEY(Id),
  INDEX ProviderSubscriptionDetails_FKIndex2(SubscriptionMaster_Id),
  INDEX ProviderSubscriptionDetails_FKIndex3(ProviderGroup_Id)
);


CREATE TABLE Seeker (
  Id REAL NOT NULL AUTO_INCREMENT,
  Gender VARCHAR(10) NULL,
  FirstName VARCHAR(100) NOT NULL,
  MiddleName VARCHAR(100) NULL DEFAULT NULL,
  LastName VARCHAR(100) NULL DEFAULT NULL,
  ContactNumber1 VARCHAR(16) NOT NULL,
  ContactNumber2 VARCHAR(16) NULL,
  ContactNumber3 VARCHAR(16) NULL,
  DateOfBirth DATE NOT NULL,
  CreationDate DATE NULL,
  UpdateDate DATE NULL,
  IsActive BIT NULL,
  NoticePeriodStartDate DATE NULL,
  NoticePeriodEndDate DATE NULL,
  IsImmediateJoinee BIT NULL,
  IsWorkingCurrently BIT NULL,
  TentativeJoiningDate DATE NULL,
  HighestQualification VARCHAR(100) NULL,
  ProfileViewCount INTEGER UNSIGNED NULL,
  PrimaryEmail VARCHAR(100) NULL,
  SecondaryEmail VARCHAR(100) NULL,
  YearsOfExperience INTEGER UNSIGNED NULL,
  SkillSets VARCHAR(1000) NULL,
  IndustryCode REAL NULL,
  PRIMARY KEY(Id)
);


CREATE TABLE SeekerDetails (
  Id REAL NOT NULL AUTO_INCREMENT,
  Seeker_Id REAL NOT NULL,
  Resume BLOB NULL,
  RegistrationDate DATE NULL,
  RegistrationType VARCHAR(10) NULL,
  PRIMARY KEY(Id),
  INDEX SeekerDetails_FKIndex1(Seeker_Id)
);


CREATE TABLE SeekerSubscriptionDetails (
  Id REAL NOT NULL AUTO_INCREMENT,
  Seeker_Id REAL NOT NULL,
  SubscriptionMaster_Id REAL NOT NULL,
  SubscriptionStartDate DATE NULL,
  SubscriptionEndDate DATE NULL,
  IsActive BIT NULL,
  CreateDate DATE NULL,
  CreatedBy VARCHAR(20) NULL,
  UpdateDate DATE NULL,
  UpdatedBy VARCHAR(20) NULL,
  PRIMARY KEY(Id),
  INDEX SeekerSubscriptionDetails_FKIndex2(SubscriptionMaster_Id),
  INDEX SeekerSubscriptionDetails_FKIndex3(Seeker_Id)
);


CREATE TABLE SubscriptionMaster (
  Id REAL NOT NULL AUTO_INCREMENT,
  SubscriptionFor VARCHAR(20) NULL,
  SubscriptionName VARCHAR(50) NULL,
  SubscriptionType VARCHAR(20) NULL,
  SubscriptionAmount REAL NULL,
  isActive BIT NULL,
  CreateDate DATE NULL,
  CreatedBy VARCHAR(25) NULL,
  UpdateDate DATE NULL,
  UpdatedBy VARCHAR(25) NULL,
  PRIMARY KEY(Id)
);


CREATE TABLE SubscriptionPaymentDetails (
  Id REAL NOT NULL AUTO_INCREMENT,
  SubscriptionMaster_Id REAL NOT NULL,
  SubscriberId REAL NULL,
  Amount REAL NULL,
  PaymentGateway VARCHAR(100) NULL,
  TransactionId VARCHAR(100) NULL,
  PaymentStatus BIT NULL,
  PaymentDate DATE NULL,
  CreatedDate DATE NULL,
  UpdatedDate DATE NULL,
  UpdatedBy REAL NULL,
  PRIMARY KEY(Id),
  INDEX SubscriptionPaymentDetails_FKIndex1(SubscriptionMaster_Id)
);


CREATE TABLE SubscriptionToIndustryDetails (
  Id REAL NOT NULL AUTO_INCREMENT,
  IndustryMaster_Id REAL NOT NULL,
  ProviderSubscriptionDetails_Id REAL NOT NULL,
  CreateDate DATE NULL,
  CreatedBy REAL NULL,
  UpdateDate DATE NULL,
  UpdatedBy REAL NULL,
  IsActive BIT NULL,
  PRIMARY KEY(Id),
  INDEX SubscriptionToIndustryDetails_FKIndex1(ProviderSubscriptionDetails_Id),
  INDEX SubscriptionToIndustryDetails_FKIndex2(IndustryMaster_Id)
);


