CREATE TABLE IF NOT EXISTS categories (
	ID SERIAL NOT NULL,
    uuid_local uuid UNIQUE DEFAULT gen_random_uuid(),
    NAME VARCHAR(255),
   	CREATED_AT TIMESTAMP WITH TIME ZONE,
	CREATED_BY VARCHAR(255),
	UPDATED_AT TIMESTAMP WITH TIME ZONE,
	UPDATED_BY VARCHAR(255),
	DELETED_AT TIMESTAMP WITH TIME ZONE,
	DELETED_BY VARCHAR(255),
	IS_DELETED INT,
    PRIMARY KEY(ID)
);

CREATE TABLE IF NOT EXISTS foods (
	ID SERIAL NOT NULL,
	uuid_local uuid UNIQUE DEFAULT gen_random_uuid(),
	NAME VARCHAR(255),
	category_uuid_local uuid,
	quantity INT,
	IMAGE VARCHAR(255),
	DESCRIPTION TEXT,
	PRICE FLOAT,
	CREATED_AT TIMESTAMP WITH TIME ZONE,
	CREATED_BY VARCHAR(255),
	UPDATED_AT TIMESTAMP WITH TIME ZONE,
	UPDATED_BY VARCHAR(255),
	DELETED_AT TIMESTAMP WITH TIME ZONE,
	DELETED_BY VARCHAR(255),
	STATUS INT,
	IS_DELETED INT,
	PRIMARY KEY(ID),
	CONSTRAINT FK_category_uuid_local
      FOREIGN KEY(category_uuid_local) 
	  REFERENCES categories(uuid_local)
);