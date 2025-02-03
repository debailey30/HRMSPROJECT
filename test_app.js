const assert = require('assert');
const { connectToDatabase, startServer } = require('./app');

describe('App Tests', function() {
    it('should connect to database', function() {
        assert.strictEqual(connectToDatabase('localhost'), undefined);
    });

    it('should start server', function() {
        assert.strictEqual(startServer(8080), undefined);
    });
});