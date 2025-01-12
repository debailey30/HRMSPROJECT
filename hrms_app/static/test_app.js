const assert = require('assert');
const { connectToDatabase, startServer, newFeature } = require('./app');

describe('App Tests', function() {
    it('should connect to database', function() {
        assert.strictEqual(connectToDatabase('localhost'), undefined);
    });

    it('should start server', function() {
        assert.strictEqual(startServer(8080), undefined);
    });

    it('should enable new feature', function() {
        assert.strictEqual(newFeature(), undefined);
    });
});