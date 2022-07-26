CREATE TABLE IF NOT EXISTS EMPLOYEE (
   ID serial UNIQUE NOT NULL,
   USERNAME VARCHAR(255) NOT NULL,
   PASSWORD VARCHAR(255) NOT NULL,
   LAST_NAME VARCHAR(255),
   FIRST_NAME VARCHAR(255),
   AVARTA VARCHAR(255),
   STATUS INT NOT NULL DEFAULT 1,
   ROLE VARCHAR(255) NOT NULL,
   token VARCHAR(255),
   refresh_token VARCHAR(255),
   CREATED_AT TIMESTAMP WITH TIME ZONE,
   CREATED_BY VARCHAR(255),
   UPDATED_AT TIMESTAMP WITH TIME ZONE,
   UPDATED_BY VARCHAR(255),
   DELETED_AT TIMESTAMP WITH TIME ZONE,
   DELETED_BY VARCHAR(255),
   PRIMARY KEY(ID)
);

-- CREATE TABLE IF NOT EXISTS CARMODEL (
--     ID VARCHAR(255) UNIQUE NOT NULL,
--     BR_ID VARCHAR(255) NOT NULL,
--     NAME VARCHAR(255),
--     PRICE FLOAT,
--     YEAR TIMESTAMP WITH TIME ZONE,
--     PRIMARY KEY(ID),
--     CONSTRAINT FK_BR_ID
--       FOREIGN KEY(BR_ID) 
--    REFERENCES CARBRAND(ID)
-- );