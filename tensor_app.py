import tensorflow as tf

flags = tf.app.flags
############################
#    hyper parameters      #
############################

# For separate margin loss
flags.DEFINE_float('m_plus', 0.9, 'the paramter of m plus')
flags.DEFINE_float('m_minus', 0.1, 'the parameter of m minus')
flags.DEFINE_float('lambda_val', 0.5, 'down weight of the loss for absent digit classes')
FLAGS = tf.app.flags.FLAGS


def main(_):
    print(FLAGS.m_plus)
    print(FLAGS.m_minus)
    # print(lambda_val)
    print(FLAGS.lambda_val)
    print(type(FLAGS))


if __name__ == '__main__':
    # main()
    # tf.app.run()
    tf.compat.v1.app.run()
    

